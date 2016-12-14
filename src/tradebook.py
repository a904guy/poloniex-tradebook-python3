import threading


class TradeBook:
    data = {}
    callbacks = {}

    def __init__(self):
        self.data = {}

    def add(self, topic, data):

        if topic not in self.data:
            self.data[topic] = []

        self.data[topic].append(data)

        if 'add_data' in self.callbacks:
            for callback in self.callbacks['add_data']:
                threading.Thread(target=callback, args=(self, data,)).start()

        return self

    def remove(self, topic, data):

        if topic not in self.data:
            return self

        if data in self.data[topic]:
            self.data[topic].remove(data)

        if 'remove_data' in self.callbacks:
            for callback in self.callbacks['remove_data']:
                threading.Thread(target=callback, args=(self, data,)).start()

        return self

    def add_callback(self, topic, callback):
        if topic not in self.callbacks:
            self.callbacks[topic] = []

        self.callbacks[topic].append(callback)

        return self

    def remove_callback(self, topic, callback):
        if topic not in self.callbacks:
            return self

        self.callbacks[topic].remove(callback)

        return self
