import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError ('List must contain nine numbers.')
  
  b = np.array(list).reshape((3,3))

  calculations = {
      'mean': [(np.mean(b, axis=0)).tolist(), (np.mean(b, axis=1)).tolist(), (np.mean(b)).tolist()],
      'variance': [(np.var(b, axis=0)).tolist(), (np.var(b, axis=1)).tolist(), np.var(b)],
      'standard deviation': [(np.std(b, axis=0)).tolist(), (np.std(b, axis=1)).tolist(), np.std(b)],
      'max': [(np.max(b, axis=0)).tolist(), (np.max(b, axis=1)).tolist(), np.max(b)],
      'min': [(np.min(b, axis=0)).tolist(), (np.min(b, axis=1)).tolist(), np.min(b)],
      'sum': [(np.sum(b, axis=0)).tolist(), (np.sum(b, axis=1)).tolist(), np.sum(b)]
    }
    
  return calculations