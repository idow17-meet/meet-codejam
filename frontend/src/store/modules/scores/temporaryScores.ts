import { Score, Problem } from '@/classes'

// Static scores here until rest api integration
const tempScores = [
  // Score #1
  new Score (
    new Problem (
      'Factorials Factory',
      10,
      'Some description',
      8000,
      '1',
    ),
  ),
  // Score #2
  new Score (
    new Problem (
      'Palindromic Number',
      37,
      'Some description noitpircsed emoS',
      18700,
      '2',
    ),
  ),
  new Score (
    new Problem (
      'Ladder Climbing',
      75,
      '#Some<br>#Description<br>#Here',
      37000,
      '3',
    ),
    37000,
  ),
]

// Static scores here until rest api integration
const tempScores2 = [
  // Score #1
  new Score (
    new Problem (
      'Factorials Factory',
      10,
      'Some description',
      8000,
      '1',
    ),
  ),
  // Score #2
  new Score (
    new Problem (
      'Palindromic Number',
      37,
      'Some description noitpircsed emoS',
      18700,
      '2',
    ),
  ),
  new Score (
    new Problem (
      'Ladder Climbing',
      75,
      '#Some<br>#Description<br>#Here',
      37000,
      '3',
    ),
    18500,
  ),
]

export {tempScores, tempScores2}
