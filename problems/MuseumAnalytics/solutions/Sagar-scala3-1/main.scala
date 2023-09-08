import scala.io.StdIn._
object Solution {
  def main(args: Array[String]): Unit = {
    val numResponses = readInt()
    val dinosaurs = List.fill(numResponses)(readLine().split(",")).flatten
    val frequencies: Map[String, Int] = dinosaurs.groupBy(identity).view.mapValues(_.size).toMap
    val belovedDinosaur = frequencies.maxBy(_._2)
    println(belovedDinosaur._1)
    println(belovedDinosaur._2)
  }
}
