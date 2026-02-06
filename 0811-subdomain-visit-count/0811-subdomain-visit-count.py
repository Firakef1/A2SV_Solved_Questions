class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        counter = {}

        for line in cpdomains:

            line = line.split()
            count = int(line[0])
            domain = line[1]
            cur_domain = domain
            state = True

            for i in range(len(domain)):

                if state:
                    if cur_domain in counter:
                        counter[cur_domain] += count
                    else:
                        counter[cur_domain] = count

                    state = False

                if domain[i] == ".":

                    cur_domain = domain[i+1:]
                    state = True

        out = []

        for key in counter.keys():
            x = f"{counter[key]} {key}"
            out.append(x)
        

        return out