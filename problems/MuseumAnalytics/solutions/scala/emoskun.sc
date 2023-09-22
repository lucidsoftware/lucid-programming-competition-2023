val beloved = scala.io.Source.stdin
  .getLines()
  .drop(1)
  .flatMap(_.split(","))
  .toList
  .groupBy(identity)
  .maxBy(_._2.length)
println(beloved._1)
println(beloved._2.length)
