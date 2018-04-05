class Reporter:
    '''abstract base class for template method pattern'''
    def __init__ (self, title, body=[]):
        self.title = title
        self.body = body

    def output_report(self):
        self.output_start()
        self.output_title()
        self.output_body_start()
        self.output_body()
        self.output_body_end()
        self.output_end()


    def output_start(self):
        print ('execute output_start')

    def output_title(self):
        print(self.title)

    def output_body_start(self):
        pass

    def output_body(self):
        for b in self.body :
            print(b)

    def output_body_end(self):
        pass

    def output_end(self):
        pass

class HTMLReporter (Reporter):
    '''Concrete class of Reporter for HTML format'''

    def output_start(self):
        print('<html>')

    def output_body_start(self):
        print('<body>')

    def output_body_end(self):
        print('</body>')

    def output_end(self):
        print('</html>')

if __name__ == '__main__':
    r = HTMLReporter('hello world', ['good', 'better', 'best'])
    r.output_report()



