package main

import (
	"math"
	"testing"
)

func TestNewProtein(t *testing.T) {
	seq := "HPHPPH"
	p := NewProtein(seq)
	
	if len(p.Sequence) != len(seq) {
		t.Errorf("Expected protein length %d, got %d", len(seq), len(p.Sequence))
	}
	
	for i, aa := range p.Sequence {
		if aa.Type != rune(seq[i]) {
			t.Errorf("At position %d: expected %c, got %c", i, seq[i], aa.Type)
		}
	}
}

func TestFold(t *testing.T) {
	p := NewProtein("HPHPPH")
	angle := math.Pi / 2 // 90 degrees
	p.Fold(angle)
	
	// Verify positions changed from initial (0,0,0)
	for i, aa := range p.Sequence {
		if i > 0 && (aa.X == 0 && aa.Y == 0) {
			t.Errorf("Position %d not folded - still at origin", i)
		}
	}
}

func TestCalculateEnergy(t *testing.T) {
	tests := []struct {
		seq    string
		angle  float64
		expect float64
	}{
		{"HH", math.Pi, -1.0},    // Two H's close together
		{"HP", math.Pi, 0.0},     // No H-H interaction
		{"HPHPPH", math.Pi/2, -1.0}, // Some H-H interactions
	}
	
	for _, tt := range tests {
		p := NewProtein(tt.seq)
		p.Fold(tt.angle)
		energy := p.CalculateEnergy()
		if math.Abs(energy-tt.expect) > 0.01 {
			t.Errorf("For %s at %.2f rad: expected %.2f, got %.2f", 
				tt.seq, tt.angle, tt.expect, energy)
		}
	}
}
