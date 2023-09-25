import scala.io.StdIn

case class Species(name: String, attributes: Set[String]) {
  def score(fossil: Fossil): Float = {
    val M = fossil.attributes.count(attributes)
    val N = fossil.attributes.size - M
    val K = attributes.size.toFloat
    100f * (M - N) / K
  }
}
object Species {
  def parse(): Species = {
    val name = StdIn.readLine()
    val numAttributes = StdIn.readInt()
    val attributes = (0 until numAttributes).map(_ => StdIn.readLine()).toSet
    Species(name, attributes)
  }
}

case class Fossil(attributes: Seq[String])
object Fossil {
  def parse(): Fossil = {
    val numAttributes = StdIn.readInt()
    val attributes = (0 until numAttributes).map(_ => StdIn.readLine())
    Fossil(attributes)
  }
}

val numSpecies = StdIn.readInt()
val allSpecies = (0 until numSpecies).map(_ => Species.parse())

val numFossils = StdIn.readInt()
(0 until numFossils).foreach { _ =>
  val fossil = Fossil.parse()
  val mostLikely = allSpecies.maxBy(_.score(fossil))
  println(
    if (mostLikely.score(fossil) >= 50f) mostLikely.name
    else "Possible New Discovery"
  )
}
