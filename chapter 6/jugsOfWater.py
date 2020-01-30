n_vertex = int(raw_input("n vertex: "))

def pCollision(n_vertex):
    p_clockwise = float(1./2)**n_vertex
    p_counter_clockwise = float(1./2)**n_vertex
    return float(1 - (p_clockwise + p_counter_clockwise)) # total - never collide

print pCollision(n_vertex)