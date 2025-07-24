package main

import (
	"fmt"
	"math"
)

type AminoAcid struct {
	Type    rune
	X, Y, Z float64
}

type Protein struct {
	Sequence []AminoAcid
}

func NewProtein(sequence string) *Protein {
	p := &Protein{}
	for _, c := range sequence {
		p.Sequence = append(p.Sequence, AminoAcid{Type: c})
	}
	return p
}

func (p *Protein) Fold(angle float64) {
	// Simple 2D folding simulation
	for i := range p.Sequence {
		if i > 0 {
			p.Sequence[i].X = p.Sequence[i-1].X + math.Cos(angle*float64(i))
			p.Sequence[i].Y = p.Sequence[i-1].Y + math.Sin(angle*float64(i))
		}
	}
}

func (p *Protein) CalculateEnergy() float64 {
	// Simple energy calculation based on hydrophobic interactions
	energy := 0.0
	for i := range p.Sequence {
		for j := i + 2; j < len(p.Sequence); j++ {
			if p.Sequence[i].Type == 'H' && p.Sequence[j].Type == 'H' {
				dist := math.Sqrt(math.Pow(p.Sequence[i].X-p.Sequence[j].X, 2) +
					math.Pow(p.Sequence[i].Y-p.Sequence[j].Y, 2))
				if dist < 1.0 {
					energy -= 1.0 // Favorable interaction
				}
			}
		}
	}
	return energy
}


func main() {
	protein := NewProtein("HPHPPHHPH")
	protein.Fold(math.Pi / 3) // 60 degree angle
	fmt.Printf("Protein energy: %.2f\n", protein.CalculateEnergy())
}

app.get('/sqrt/:n', (req, res) => {
const n = parseFloat(req.params.n);

// Add error handling for NaN and less than zero. AI!

const result = math.sqrt(n);
res.json({ result: result });
});

