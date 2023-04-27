The pattern below swaps the least frequent numer to the next in the alphabet. Complete the pattern.

[ a a c b b][ a a d b b ]
[ d m m m n n ][ e m m m n n ]
[ x x p j j ][ x x q j j ]

* this failed without the prompt but succeeded with it

The transformation swaps the least-frequent letter for the next in the alphabet.

a a c b b -- changes to --> a a d b b
d m m m n n -- changes to --> e m m m n n
o o i i i i i w j j -- changes to --> o o j i i i i x j j


a b b c c c -- changes to --> c c c b b a
u u i i i i i j j j s -- changes to --> i i i i i j j j u u s
z z y y y d -- changes to --> y y y z z d


1st-order operations
successor ✅
reflect ✅
delete ✅
duplicate ✅ 
expand-around ✅
swap positions ✅ 
capitalize (definitely seems to struggle)

groupings / identities
- character match (e.g. "a")
- position ? (nth-posiiton)
- occurs N times (size-N)
- most/least (frequent)
- first/last (position, alphabetical)
- before/after
- recurring-n-times (e.g. aaxxjjaacc --> bbxxjjbbcc)

e.g. combining into 2nd-order

successor of least-frequent letter
successor of most-frequent letter
successor of last alphabetical letter
successor of first alphabetical letter

reflect around least-frequent letter
reflect around most-frequent letter
reflect around last alphabetical letter
reflect around first alphabetical letter

delete least-frequent letter
delete most-frequent letter
delete last alphabetical letter
delete first alphabetical letter

duplicate least-frequent letter
duplicate most-frequent letter
duplicate last alphabetical letter
duplicate first alphabetical letter

swap positions of least-frequent letter and most-frequent letter group
swap positions of most-frequent letter and first alphabetical letter group
swap positions of most-frequent letter and last alphabetical letter group
swap positions of least-frequent letter and last alphabetical letter group
swap positions of least-frequent letter and first alphabetical letter group
swap positions of first and last alphabetical groups

alphabetize groups 
sort groups by size (ascending/descending)


successor of group after largest group (4th order?)
successor of group after size-3 group (3rd order?)


size 3 group = 1st order: where size(group) == 3
largest group = 2nd order: where size(group) == max(size(groups)) 
after largest group = 3rd order: where before(size(group)) == max(size(groups)) (idk the notation here)


size-is(x, 3) --> identifies a group - 1st order

largest(x) = size-is(x, max(sizes(x)))

same-size(group(x), group(y))


**so actually**: can get a lot just with the group selections in terms of the higher-order-ness of relations. 

----

Can define functions to execute each of the operations and to extract each of the groupings. Then can compose them together to create the second order transformations listed.

Could also possibly create some kind of probabilistic grammar model to evaluate whether the prompts are sufficiently identifying the transformation and/or whether GPT-3's outputs are reasonable. If I were looking to learn things, would be a good way to learn about PGG models.

These are all sort of similar to some of Abstraction and Reasoning Corpus (ARC), though not as challenging. 

## take some examples:

aabbbc --> aabbbd 
Could be: 
- (successor, last in sequence)
- (successor, last alphabetically)
- (successor, "c")
- (successor, smallest)
- (successor, size-1)
- (successor, after-largest)
- (successor, after-"b")
- (successor, after-size-3)

aabbbc --> aabbbd 
bbcccddd --> ccccddd

Could be: 
- (successor, smallest)


aabbbc --> aabbbd 
bbccccddf --> bbcccceef

Could be: 
- (successor, after-largest)
