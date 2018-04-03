
class Report:
    '''Strategy Patterにおける Context クラス'''
    def __init__(self, formatter, title, body = []):
        self.formatter = formatter
        self.title = title
        self.body = body

    def output(self):
        self.formatter.output(self)

class Formatter:
    '''Strategy Pattern の抽象基底クラス'''
    def output(self, report):
        self.output_start()
        self.output_title(report.title)
        self.output_body_start()
        self.output_body(report.body)
        self.output_body_end()
        self.output_end()

    def output_start(self): pass
    def output_title(self, title): pass
    def output_body_start(self): pass
    def output_body(self, body): pass
    def output_body_end(self): pass
    def output_end(self): pass

class HTMLFormatter (Formatter):
    '''HTML形式を適用する具象クラス'''
    def output_start(self):
        print('<html>')

    def output_title(self, title):
        print('<head><title>{0}</title></head>'.format(title))

    def output_body_start(self):
        print('<body>')

    def output_body(self, body):
        for b in body:
            print('<p>{0}</p>'.format(b))

    def output_body_end(self):
        print('</body>')

    def output_end(self):
        print('</html>')

class MDFormatter (Formatter):
    '''Markdown形式を適用する具象クラス'''
    def output_start(self): pass
    def output_title(self, title):
        print('#{0}'.format(title))
    def output_body_start(self): pass
    def output_body(self, body):
        for b in body:
            print(b)
            print('')
    def output_body_end(self): pass
    def output_end(self): pass

if __name__ == '__main__':
    print('HTML format')
    r = Report(HTMLFormatter(), 'Hello world', ['design pattern ', 'python' ])
    r.output()

    print('Markdown format')
    r.formatter = MDFormatter()
    r.output()



