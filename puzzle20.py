from collections import defaultdict
import sys

def abssum(vec):
    return abs(vec[0]) + abs(vec[1]) + abs(vec[2])

def parse(line, idx):
    def parseValues(data):
        start = data.find('<')+1
        end = data.find('>', start)
        data = data[start:end]
        nums = data.split(',')
        return (int(nums[0]), int(nums[1]), int(nums[2]))
    data = line.split(", ")
    pos = parseValues(data[0])
    v = parseValues(data[1])
    a = parseValues(data[2])
    return {'pos': pos, 'vel': v, 'acc': a, 'dist': abssum(pos), 'idx': idx}

def add(vec1, vec2):
    return (vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2])

def distance(vec1, vec2):
    return sum([abs(vec2[0]-vec1[0]), abs(vec2[1]-vec1[1]), abs(vec2[2]-vec1[2])])

def doit(lines):
    particles = [parse(line, i) for (i,line) in enumerate(lines)]
    origin = (0,0,0)
    # This only works because my input is 'suitable', there are cases where it'll produce
    # the wrong  result or only provides a smaller search space
    accelerations = [(distance(origin, p['acc']), p["acc"], i) for (i,p) in enumerate(particles)]
    accelerations.sort()
    part1 = accelerations[:5]
    iter = 0
    while True:
        for particle in particles:
            particle['vel'] = add(particle['vel'], particle['acc'])
            particle['pos'] = add(particle['pos'], particle['vel'])
            particle['dist'] = distance(origin, particle['pos'])
        collisions = defaultdict(list)
        for (i, particle) in enumerate(particles):
            collisions[particle['pos']].append(i)
        particlestoremove = []
        for collisionlist in collisions.values():
            if len(collisionlist) > 1:
                particlestoremove += collisionlist
        particlestoremove.sort()
        particlestoremove.reverse()
        #print "colliding", particlestoremove
        for idx in particlestoremove:
            del particles[idx]
        #print "clean particles", particles
        if iter == 50:
            break
        iter += 1
        print iter, len(particles)
    part2 = len(particles), [p['idx'] for p in particles]
    return {"part1":part1, "part2":part2}
if __name__ == "__main__":
    print doit(sys.stdin.readlines())
