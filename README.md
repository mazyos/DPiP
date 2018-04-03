# DPiP
Design Pattern in Python

Russ Olsen著 "Design Pattern in Ruby" を Python の勉強を兼ねて、「PythonらしくDesign Patternを利用するとどうなるか」を試行して考察してみる。

## Template Method
ロジック（処理の流れ）から処理の詳細を分離してサブクラスに隠ぺいするパターン。サブクラスは、処理の流れではなく、手続きの詳細だけに集中すればよい。また、クラスの利用者に対しても処理の流れを隠蔽させることができる。

しかし、Pythonでは、private メソッドはあっても protected にあたるスコープがないために、クラス利用者に対して内部手続きのためのメソッドまで公開されてしまい、クラスインタフェースが簡潔にならない。

## Strategy
Template Pattern の発展形ともいえるパターン。Template Pattern ではロジックと処理対象であるデータが混在しているが、このパターンではその両者を分離している。そうすることで、ロジックの実行直前までロジックの選択を遅らせられるメリットも得られる。

Pythonもまた動的型付け言語なのでRuby同様に DuckTyping を利用できるため、ロジックを Template Pattern で縛る必要がなければ、抽象基底クラスを継承させなくても構わない。

## Observer