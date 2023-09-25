import scala.annotation.tailrec
import scala.io.StdIn.readLine

def getPoint(p: String): (Int, Int) = {
  val Point = raw"(-?\d+) (-?\d+)".r
  p match {
    case Point(x, y) =>
      (x.toInt, y.toInt)
  }
}

@tailrec
def getGCD(a: Int, b: Int): Int = {
  if (b == 0) a else getGCD(b, a % b)
}


val (fireX, fireY) = getPoint(readLine())
val count = readLine().toInt

val dinos = (1 to count)
  .map { _ => readLine() }
  .map(getPoint)

val canSee = dinos
  .map { case (x, y) =>
    val relX = x - fireX
    val relY = y - fireY
    val gcd = Math.abs(getGCD(relX, relY))
    (relX / gcd, relY / gcd)
  }
  .distinct
  .size

println(canSee)