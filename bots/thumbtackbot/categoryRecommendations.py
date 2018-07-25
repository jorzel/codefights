"""
Medium

Codewriting

4000

As you might already know, Thumbtack helps Professionals (Pros) grow their business by identifying new customers. Upon registering on Thumbtack, Pros must select categories that match the type of services they provide. To make this step easier for Pros, Thumbtack would like to provide smart suggestions of categories that usually accompany those the Pro has already selected. To do this, Thumbtack engineers analyze historical user requestData and categories in proSelections using a Jaccard index statistic.

Your task is to implement the following algorithm that returns a single category recommendation:

for each request from requestData:
calculate the Jaccard index of this request and proSelections;
Assign a score to each category that is present in the request but not in proSelections equal to the value of the Jaccard index;
divide each score by the number of summands it was obtained from;
return the category with the highest positive score. If several categories have the same positive score, return the lexicographically smallest one. If there are no categories with positive score, return an empty string instead.
Example

For

requestData = [["Accounting", "Administrative Support", "Advertising", 
                              "Bodyguard", "Auctioneering"],
               ["Accounting", "Administrative Support"],
               ["Advertising", "Auctioneering", "Bodyguard"],
               ["Bodyguard", "Services Business", "Consulting"]]
and proSelections = ["Accounting", "Advertising"], the output should be
categoryRecommendations(requestData, proSelections) = "Administrative Support".

Here's how scores are calculated:
* i = 0: Jaccard index equals 2/5 and should be added to "Administrative Support", "Bodyguard", "Auctioneering";
* i = 1: Jaccard index equals 1/3 and should be added to "Administrative Support";
* i = 2: Jaccard index equals 1/4 and should be added to "Auctioneering", "Bodyguard";
* i = 3: Jaccard index equals 0 and should be added to "Bodyguard", "Services Business", "Consulting";

So the final scores equal:
* "Administrative Support": (2/5 + 1/3) / 2 = 11/30;
* "Auctioneering": (2/5 + 1/4) / 2 = 13/40;
* "Bodyguard": (2/5 + 1/4 + 0) / 3 = 13/60;
* "Consulting": 0/1 = 0;
* "Services Business": 0/1 = 0.

For

requestData = [["Accounting", "Bodyguard"],
               ["Accounting", "Auctioneering"]]
and proSelections = ["Accounting"], the output should be
categoryRecommendations(requestData, proSelections) = "Auctioneering".

"Auctioneering" and "Bodyguard" have the same score, but "Auctioneering" is lexicographically smaller than "Bodyguard".

For requestData = [["Bodyguard"]] and proSelections = ["Bodyguard"], the output should be
categoryRecommendations(requestData, proSelections) = "".
"""




def get_jaccard(a, b):
    a = set(a)
    b = set(b)
    intesection = len(a.intersection(b))
    union = len(a) + len(b) - intesection
    return intesection / float(union)

def categoryRecommendations(requestData, proSelections):
    jaccards = []
    counter = {}
    for i, request in enumerate(requestData):
        jaccards.append(get_jaccard(request, proSelections))
        for item in request:
            if item not in proSelections:
                if item not in counter:
                    counter[item] = [1, [i]]
                else:
                    counter[item][0] += 1
                    counter[item][1].append(i)
    results = []
    for name, counts in counter.iteritems():
        score = 0
        for index in counts[1]:
            score += jaccards[index]
        score = score / float(counts[0])
        results.append([score, name])
    if results:
        winner = sorted(results, key=lambda x: (-x[0], x[1]))[0]
        if winner[0] > 0:
            return winner[1]
    return ""