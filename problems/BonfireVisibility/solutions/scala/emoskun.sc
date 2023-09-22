def parse(str: String, origin: (Int, Int)): (Int, Int) = {
  str match {
    case s"$x $y" => (x.toInt - origin._1, y.toInt - origin._2)
  }
}

def simplify(rat: (Int, Int)): (Int, Int) = {
  @scala.annotation.tailrec
  def gcd(a: Int, b: Int): Int = {
    if (b == 0) Math.abs(a) else gcd(b, a % b)
  }
  val g = gcd(rat._1, rat._2)
  (rat._1 / g, rat._2 / g)
}

val input = scala.io.Source.stdin.getLines()
val fire = parse(input.next(), (0, 0))
val dinos = input.drop(1).map(parse(_, fire))
println(dinos.distinctBy(simplify).length)
