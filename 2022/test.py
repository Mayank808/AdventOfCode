test = """Monkey 0:
  Starting items: 71, 86
  Operation: new = old * 13
  Test: divisible by 19
    If true: throw to monkey 6
    If false: throw to monkey 7

Monkey 1:
  Starting items: 66, 50, 90, 53, 88, 85
  Operation: new = old + 3
  Test: divisible by 2
    If true: throw to monkey 5
    If false: throw to monkey 4

Monkey 2:
  Starting items: 97, 54, 89, 62, 84, 80, 63
  Operation: new = old + 6
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 1

Monkey 3:
  Starting items: 82, 97, 56, 92
  Operation: new = old + 2
  Test: divisible by 5
    If true: throw to monkey 6
    If false: throw to monkey 0

Monkey 4:
  Starting items: 50, 99, 67, 61, 86
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 5:
  Starting items: 61, 66, 72, 55, 64, 53, 72, 63
  Operation: new = old + 4
  Test: divisible by 11
    If true: throw to monkey 3
    If false: throw to monkey 0

Monkey 6:
  Starting items: 59, 79, 63
  Operation: new = old * 7
  Test: divisible by 17
    If true: throw to monkey 2
    If false: throw to monkey 7

Monkey 7:
  Starting items: 55
  Operation: new = old + 7
  Test: divisible by 3
    If true: throw to monkey 2
    If false: throw to monkey 1"""
