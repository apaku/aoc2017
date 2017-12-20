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

def distances(particles):
    distances = []
    for i in range(len(particles) - 1):
        particledistances = []
        for j in range(i+1,len(particles)):
            particledistances.append(distance(particles[i]['pos'], particles[j]['pos']))
        distances.append(particledistances)
    return distances

def hasapproachingparticles(old_distances, new_distances):
    assert len(old_distances) == len(new_distances)
    for i in range(len(old_distances)):
        assert len(old_distances[i]) == len(new_distances[i])
        for j in range(len(old_distances[i])):
            old_distance = old_distances[i][j]
            new_distance = new_distances[i][j]
            if new_distance < old_distance:
                return True
    return False

def doit(lines):
    particles = [parse(line, i) for (i,line) in enumerate(lines)]
    origin = (0,0,0)
    # This only works because my input is 'suitable', there are cases where it'll produce
    # the wrong  result or only provides a smaller search space
    accelerations = [(distance(origin, p['acc']), p["acc"], i) for (i,p) in enumerate(particles)]
    accelerations.sort()
    part1 = accelerations[:5]
    # Formula: pt = .5 * a0 * t ^ 2 + v0 * t + p0
    last_distances = distances(particles)
    iter = 0
    while True:
        print "iteration", iter
        iter += 1
        for particle in particles:
            particle['vel'] = add(particle['vel'], particle['acc'])
            particle['pos'] = add(particle['pos'], particle['vel'])
            particle['dist'] = distance(origin, particle['pos'])
        new_distances = distances(particles)
        print "old", last_distances
        print "new", new_distances
        collidingparticleindexes = set()
        for i in range(len(new_distances)):
            if i in collidingparticleindexes:
                continue
            for j in range(len(new_distances[i])):
                if new_distances[i][j] == 0:
                    collidingparticleindexes.add(i)
                    collidingparticleindexes.add(j + i + 1)
        indexestoremove = list(collidingparticleindexes)
        indexestoremove.sort()
        indexestoremove.reverse()
        print "colliding", indexestoremove
        for idx in indexestoremove:
            del particles[idx]
        print "clean particles", particles
        if not hasapproachingparticles(last_distances, new_distances) or len(particles) == 1:
            break
        last_distances = new_distances
    part2 = len(particles), [p['idx'] for p in particles]
    return {"part1":part1, "part2":part2}
if __name__ == "__main__":
    print doit(sys.stdin.readlines())
