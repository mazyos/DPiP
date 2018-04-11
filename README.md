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
オブジェクトの変更を他のオブジェクトでハンドルする際のパターン。

Rubyは単一継承しかサポートしないので、パターンの実装をMixInを使用して取り込むが、Pythonでは多重継承を使ってこれを行う。通知を受け取るConsumerが単純に通知を受け取るだけならば、Pythonでも無名関数を使用できるので、それを使用すると簡素な実装となる。

## Composite
入れ子構造を扱うパターン。
ファイルとフォルダのように中身と箱を同じように扱う場合に利用する。
特にPythonらしい実装となる部分は無いかな。

## Iterator
外部イテレータ
繰り返いし対象のオブジェクトではないオブジェクトが要素を提供する

内部イテレータ
対象オブジェクト自体が内部要素の巡回を実施する

## Command

## Adapter

## Proxy

## Decorator

## Singleton

## Factory

## Builder

## Interpreter