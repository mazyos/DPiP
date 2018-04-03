# DPiP
Design Pattern in Python

Russ Olsen著 "Design Pattern in Ruby" を Python の勉強を兼ねて、「PythonらしくDesign Patternを利用するとどうなるか」を試行して考察してみる。

## Template Method
ロジック（処理の流れ）から処理の詳細を分離してサブクラスに隠ぺいするパターン。サブクラスは、処理の流れではなく、手続きの詳細だけに集中すればよい。また、クラスの利用者に対しても処理の流れを隠蔽させることができる。

しかし、Pythonでは、private メソッドはあっても protected にあたるスコープがないために、クラス利用者に対して内部手続きのためのメソッドまで公開されてしまい、クラスインタフェースが簡潔にならない。

## Strategy

## Observer