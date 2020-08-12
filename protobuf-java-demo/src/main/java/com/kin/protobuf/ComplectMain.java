package com.kin.protobuf;

import example.complex.Complex.DummyMessage;
import example.complex.Complex.ComplexMessage;

public class ComplectMain {
    public static void main(String[] args) {
        System.out.println("complex object");
        ComplexMessage.Builder builder = ComplexMessage.newBuilder();
        builder.setOneDummy(createOneDummy(7,"test7"));
        builder.addMultipleDummy(createOneDummy(8,"test8"))
                .addMultipleDummy(createOneDummy(9,"test9"));
        ComplexMessage msg = builder.build();
        System.out.println(msg);
    }
    public static  DummyMessage createOneDummy(Integer id,String name){
        DummyMessage.Builder dBuilder = DummyMessage.newBuilder();
        dBuilder.setId(id)
                .setName(name);
        return dBuilder.build();
    }
}
