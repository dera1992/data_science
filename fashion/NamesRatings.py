from mrjob.job import MRJob
from mrjob.step import MRStep


class NamesRatings(MRJob):
   def steps(self):
        return[
            MRStep(mapper=self.mapper_get,
                  reducer=self.reducer_count)
        ]

   def mapper_get(self, _, line):
       details = line.split(",")
       yield details[1], (float(details[5]),details[2])


   def reducer_count(self, key, values):
      yield key, max(values)

if __name__ == "__main__":
    NamesRatings.run()
