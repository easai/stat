import unittest
import mean
import numpy as np

class MyTestCase(unittest.TestCase):
    def test_something(self):
        x = [.2, -.1, -1.9, -.4, -1.8]
        npX = np.array(x)
        self.assertEqual(mean.sample_mean(x), np.mean(npX))
        self.assertEqual(mean.sample_variance(x), np.var(npX))
        A=[[1.0,0],
            [0,0.5]]
        npA = np.array(A)
        # self.assertEqual(np.array(mean.mat_add(A,A)), npA+npA)

if __name__ == '__main__':
    unittest.main()
