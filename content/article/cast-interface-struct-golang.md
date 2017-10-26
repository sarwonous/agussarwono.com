+++
categories = [""]
date = "2017-10-25T15:45:42+07:00"
draft = false
tags = [""]
title = "cast interface struct golang"

+++

cast interface in golang can be usefull when you make a modular app using golang

says

{{< highlight go "linenos=table,hl_lines=8 15-17" >}}
package main

import(
	"fmt"
)

type Bird interface {
	Fly()
}

type Parrot struct {
	Bird
	Name string
}

func (p *Parrot) Fly() {
	fmt.Println("a Parrot name " + p.Name + " flying")
}

type Dove struct {
	Bird
	Name string
}

func (p *Dove) Fly() {
	fmt.Println("a Dove name " + p.Name + " flying")
}


func NewBird(birdType string, name string) Bird {
	var bird Bird
	switch birdType {
	case "dove":
		bird = &Dove{
			Name: name,
		}
	case "parrot":
		bird = &Parrot{
			Name: name,
		}
	default:
	}

	return bird;
}

func main(){
	dove := NewBird("dove", "Doval")
	parrot := NewBird("parrot", "Patriot")
	// to access Name in dove, cast dove to type Dove
	doveBird, valid := dove.(*Dove)
	if !valid {
		panic("invalid type")
	}
	fmt.Println(doveBird.Name)
	doveBird.Fly()
	// same as dove, you need to cast parrot
	parrotBird, valid := parrot.(*Parrot)
	if !valid {
		panic("invalid type")
	}
	fmt.Println(parrotBird.Name)
	parrotBird.Fly()
}
{{< / highlight >}}