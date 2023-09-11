from mrjob.job import MRJob
from mrjob.step import MRStep


class SortBrandPrice(MRJob):
   def steps(self):
        return[
            MRStep(mapper=self.mapper_get,
                  reducer=self.reducer_count),
            MRStep(reducer=self.select_top5)
        ]

   def mapper_get(self, _, line):
       details = line.split(",")
       yield details[4], float(details[2])


   def reducer_count(self, key, values):
      yield None, (sum(values),key)

   def select_top5(self, _, pair):
      sorted_pairs = sorted(pair, reverse=True)
      for pair in sorted_pairs[0:5]:
        yield pair

if __name__ == "__main__":
    SortBrandPrice.run()
