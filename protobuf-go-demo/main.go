package main

import (
	"fmt"
	"io/ioutil"
	"log"

	complexpb "example.com/protos/protos/complex"
	enumpb "example.com/protos/protos/enum"
	simplepb "example.com/protos/protos/simple"

	"github.com/golang/protobuf/jsonpb"

	"github.com/golang/protobuf/proto"
)

func main() {
	fmt.Println("hello")
	sm := aboutSimple()
	fmt.Println("-----file demo-----")
	// write to file
	writeToFile("simple.bin", sm)
	// read from file
	sm2 := simplepb.SimpleMessage{}
	readFromFile("simple.bin", &sm2)
	printPb(sm2)

	fmt.Println("-----json demo-----")
	// parse to json
	json := toJSON(sm)
	fmt.Println(json)
	// parse from json
	sm3 := simplepb.SimpleMessage{}
	fromJSON(json, &sm3)
	printPb(sm3)

	fmt.Println("-----enum demo-----")
	em := enumpb.EnumMessage{
		Id:           777,
		DayOfTheWeek: enumpb.DayOfTheWeek_TUESDAY,
	}
	fmt.Println(toJSON(&em))

	fmt.Println("-----complex demo-----")
	dm1 := complexpb.DummyMessage{
		Id:   1,
		Name: "test1",
	}
	dm2 := complexpb.DummyMessage{
		Id:   2,
		Name: "test2",
	}
	dm3 := complexpb.DummyMessage{
		Id:   3,
		Name: "test3",
	}
	cm := complexpb.ComplexMessage{
		OneDummy:      &dm1,
		MultipleDummy: []*complexpb.DummyMessage{&dm2, &dm3},
	}
	fmt.Println(toJSON(&cm))

}
func toJSON(pb proto.Message) string {
	marshaler := jsonpb.Marshaler{}
	out, err := marshaler.MarshalToString(pb)
	if err != nil {
		log.Fatalln("Can't serialize the message to json", err)
		return ""
	}
	return out
}
func fromJSON(json string, pb proto.Message) error {
	if err := jsonpb.UnmarshalString(json, pb); err != nil {
		log.Fatalln("Can't serialize the message to json", err)
		return err
	}
	return nil
}
func writeToFile(fname string, pb proto.Message) error {
	out, err := proto.Marshal(pb)
	if err != nil {
		log.Fatalln("Can't serialize the message", err)
		return err
	}
	if err := ioutil.WriteFile(fname, out, 0644); err != nil {
		log.Fatalln("Can't write to file", err)
		return err
	}
	return nil
}
func readFromFile(fname string, pb proto.Message) error {
	in, err := ioutil.ReadFile(fname)
	if err != nil {
		log.Fatalln("Can't read from file", err)
		return err
	}
	if err2 := proto.Unmarshal(in, pb); err2 != nil {
		log.Fatalln("Can't deserialize the message", err2)
		return err2
	}
	return nil
}
func aboutSimple() *simplepb.SimpleMessage {
	sm := simplepb.SimpleMessage{
		Id:         123,
		IsSimple:   false,
		Name:       "test name",
		SampleList: []int32{1, 3, 5},
	}
	printPb(sm)
	return &sm
}
func printPb(sm simplepb.SimpleMessage) {
	fmt.Println(sm.GetId())
	fmt.Println(sm.GetName())
	fmt.Println(sm.GetIsSimple())
	fmt.Println(sm.GetSampleList())
}
