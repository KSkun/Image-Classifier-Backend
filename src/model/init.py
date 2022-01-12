from model.task import init_spider_stream, init_classifier_stream


def init_model():
    # init spider & classifier streams
    init_spider_stream()
    init_classifier_stream()
