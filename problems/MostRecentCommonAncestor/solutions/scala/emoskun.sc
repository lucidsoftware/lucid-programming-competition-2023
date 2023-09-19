import scala.annotation.tailrec
import scala.io.Source.stdin

def parseAncestryTree(
    arrows: List[String]
): Map[String, String] = {
  arrows.map {
    _ match {
      case s"$ancestor -- $descendant" => descendant -> ancestor
    }
  }.toMap
}

def mostRecentCommonAncestor(
    first: String,
    second: String,
    immediateAncestors: Map[String, String]
): String = {
  val alsoSecond = allAncestors(second, immediateAncestors).toSet
  allAncestors(first, immediateAncestors).find(alsoSecond).get
}

def allAncestors(
    dinosaur: String,
    immediateAncestors: Map[String, String]
): Vector[String] = {
  @tailrec def ancestors(
      current: String,
      accumulator: Vector[String]
  ): Vector[String] = {
    immediateAncestors.get(current) match {
      case Some(ancestor) => ancestors(ancestor, accumulator :+ ancestor)
      case None           => accumulator
    }
  }
  ancestors(dinosaur, Vector(dinosaur))
}

val input = stdin.getLines().drop(1).toList
val (arrows, dinosaurs) = input.splitAt(input.length - 2)
val immediateAncestors = parseAncestryTree(arrows)
val first = dinosaurs(0)
val second = dinosaurs(1)

println(mostRecentCommonAncestor(first, second, immediateAncestors))
