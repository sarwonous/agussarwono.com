+++
categories = ["tips"]
date = "2017-10-25T15:45:42+07:00"
draft = false
tags = ["golang","programming"]
title = "Cast an interface/struct in golang"
description = "cast interface in golang can be usefull when you make a modular app using golang..."

+++

type casting interface in golang can be useful when you build a modular app using golang

says
{{< highlight go >}}
package main

import (
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

	return bird
}

func main() {
	bird1 := NewBird("dove", "Doval")
	bird2 := NewBird("parrot", "Patriot")
	// to access Name in bird1, cast dove to type Dove
	dove, valid := bird1.(*Dove)
	if !valid {
		panic("invalid type")
	}
	fmt.Println(dove.Name)
	dove.Fly()
	// same as dove, you need to cast bird2
	parrot, valid := bird2.(*Parrot)
	if !valid {
		panic("invalid type")
	}
	fmt.Println(parrot.Name)
	parrot.Fly()
}

{{< / highlight >}}

above example would return 

```shell
machine@root$
Doval
a Dove name Doval flying
Patriot
a Parrot name Patriot flying

```

as you can see, you need to cast `dove` to `Dove` type to access `Name` property, that because `NewBird` only return interface `Bird` which doesn't have `Name` property, you can only define method inside interface, therefore you need to cast them