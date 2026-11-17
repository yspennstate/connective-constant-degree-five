# The connective constant of non-simple transitive graphs of degree five

Yitzchak Shmalo

Grimmett and Li (Combinatorica 35 (2015), 279–294) proved that the connective constant μ of an infinite, connected,
Δ-regular, vertex-transitive graph satisfies μ ≥ √(Δ − 1) when the graph is simple, and also when it has multiple
edges and Δ ≤ 4. They asked whether the second statement holds for Δ ≥ 5. The paper proves it for Δ = 5: every
infinite, connected, 5-regular, vertex-transitive, loopless multigraph has μ ≥ 2, with equality for the bridge graph.
The proof passes to the quotient by the atoms, the smallest finite vertex sets with the fewest boundary edges, where the
branching inequality of Grimmett and Li holds, lifts walks of the quotient to walks of the graph with weights counted by self-avoiding paths inside the
atoms, and reduces the bound to a convexity condition on the atoms alone. The four atom types of degree five satisfy
it.

## Contents

- `paper/main.tex`, `paper/main.pdf` – the paper.
- `code/delta5_check.py` – the program of Section 5 (Python 3, standard library only).
- `code/delta5_check.out` – its output.
- `SHA256SUMS` – checksums of the files above.

## Reproducing Section 5

```
python code/delta5_check.py
```

For each of the four atom types (a, e) = (2, 1), (2, 2), (3, 1), (4, 1) the program lists the labelled loopless
multigraphs allowed by Lemma 3.1(4), computes the path sums exactly with fractions, and prints the least value of
ψ(c) over shapes and entry vertices: 0, 0, (1/2) log 2 and (1/2) log 3. It runs in about a second.

## License

Paper: CC BY 4.0. Code: MIT.
