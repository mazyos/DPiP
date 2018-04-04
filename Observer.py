class SimpleObservable:
    '''Observer Patterの実装#1
関数オブジェクトを使った簡素な実装'''

    def __init__(self):
        self.subscriber = []
        self.attrib = 'default value'

    def add_subscriber(self, subscriber):
        '''sub: 1引数 関数 引数は通知対象属性の値'''
        self.subscriber.append(subscriber)

    def update(self, val):
        self.attrib = val
        self.notify()

    def get(self):
        return self.attrib

    def notify(self):
        for s in self.subscriber:
            s(self.attrib)

class ObservableMixIn (object):
    '''Observer PatternのMixIn実装'''
    def __init__(self):
        self.subscriber = []
        self.update_flag = False

    def add_subscriber(self, sub):
        '''sub: 1引数 関数 引数はこのクラスを継承したサブクラスのインスタンス'''
        self.subscriber.append(sub)

    def remove_subscriber(self, sub):
        self.subscriber.remove(sub)

    def notify(self):
        '''Subscriberに変更を通知する。
        事前にupdated メソッドを呼び出していれば通知され、いなければ通知されない（変更がなかったため）。
        実行後 updated フラグはFalseに戻される。'''
        if not self.update_flag: return
        for s in self.subscriber:
            s(self)
        self.update_flag = False

    def updated(self):
        self.update_flag = True

class Subject2 (ObservableMixIn):
    def __init__(self):
        super().__init__()
        self.attrib = 'hello world!'

    def set_attrib(self, val):
        self.attrib = val
        self.updated()
        self.notify()

    def get_attrib(self):
        return self.attrib

if __name__ == '__main__':
    print('Simple Observer')
    subject = SimpleObservable()
    print('initial value: {0}'.format(subject.get()))
    subject.add_subscriber(lambda x: print('#1 get notification "{0}"'.format(x)))
    subject.add_subscriber(lambda x: print('#2 get notification "{0}"'.format(x)))
    subject.update('new value')

    print('Mixin Observer')
    subject = Subject2()
    print('initial value: {0}'.format(subject.get_attrib()))
    subject.add_subscriber(lambda x: print('#1 get notification "{0}"'.format(x.get_attrib())))
    subject.add_subscriber(lambda x: print('#2 get notification "{0}"'.format(x.get_attrib())))
    subject.set_attrib('HELLO PYTHON')

