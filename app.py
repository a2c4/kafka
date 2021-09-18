from _imports import *
from _constants import *

def get_kafka_client():
    return KafkaClient(hosts=KAFKA_SERVER_PORT)

app = Flask(__name__,template_folder=PROJECT_DIR_LOC)

@app.route('/')
def index():
    return render_template('index.html')

counter = 0
@app.route("/history")
def listen():
    topicname = KAFKA_TOPIC_NAME
    client = get_kafka_client()
    topic = client.topics[topicname]
    consumer = topic.get_simple_consumer(auto_offset_reset=OffsetType.LATEST,reset_offset_on_start=True)
    MAX_PARTITION_REWIND = int(math.ceil(LAST_N_MESSAGES / len(consumer._partitions)))
    offsets = [(p, op.last_offset_consumed - MAX_PARTITION_REWIND) for p, op in consumer._partitions.items()]
    offsets = [(p, (o if o > -1 else -2)) for p, o in offsets]
    consumer.reset_offsets(offsets)
    def events():
        while(True):
            data_arr = []
            for i in islice(consumer, LAST_N_MESSAGES):
                global counter
                counter += 1
                payload=json.loads(i.value)
                data_arr.append(str(i.value))
                update_db(i.value.hex())
                _data = json.dumps({ "data":data_arr, "counter":str(counter)})
                yield f"id: {str(counter)}\ndata: {_data}\nevent: online\n\n"
                time.sleep(1)
    return Response(events(), mimetype='text/event-stream')

if __name__ == "__main__":
    # app.run(port=80, debug=True)
    http_server = WSGIServer((WEBAPP_SERVER, WEBAPP_PORT), app)
    http_server.serve_forever()
