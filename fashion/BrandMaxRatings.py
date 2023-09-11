from mrjob.job import MRJob
from mrjob.step import MRStep


class BrandMaxRatings(MRJob):
   def steps(self):
        return[
            MRStep(mapper=self.mapper_get,
                  reducer=self.reducer_count)
        ]

   def mapper_get(self, _, line):
       details = line.split(",")
       yield details[4],details[5]


   def reducer_count(self, key, values):
      yield key, max(values)

if __name__ == "__main__":
    BrandMaxRatings.run()
