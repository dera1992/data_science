from mrjob.job import MRJob
from mrjob.step import MRStep


class RatingBreakdown(MRJob):
   def steps(self):
        return[
            MRStep(mapper=self.mapper_get,
                  reducer=self.reducer_count)
        ]

   def mapper_get(self, _, line):
       details = line.split(",")
       yield details[5], 1


   def reducer_count(self, key, values):
      yield key, sum(values)

if __name__ == "__main__":
    RatingBreakdown.run()
