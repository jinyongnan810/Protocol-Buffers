package com.kin.protobuf;

import com.google.protobuf.InvalidProtocolBufferException;
import com.google.protobuf.util.JsonFormat;
import example.complex.Complex;
import example.simple.Simple;

public class ProtoToJSON {
    public static void main(String[] args) throws InvalidProtocolBufferException {
        System.out.println("complex object");
        Complex.ComplexMessage.Builder builder = Complex.ComplexMessage.newBuilder();
        builder.setOneDummy(createOneDummy(7,"test7"));
        builder.addMultipleDummy(createOneDummy(8,"test8"))
                .addMultipleDummy(createOneDummy(9,"test9"));
        Complex.ComplexMessage msg = builder.build();
        System.out.println(msg);
        // convert proto to json
        String json = JsonFormat.printer().print(builder);
        System.out.println(json);
        // convert json to proto
        Complex.ComplexMessage.Builder builder2 = Complex.ComplexMessage.newBuilder();
        JsonFormat.parser().ignoringUnknownFields().merge(json, builder2);
        System.out.println(builder2.build());
    }
    public static Complex.DummyMessage createOneDummy(Integer id, String name){
        Complex.DummyMessage.Builder dBuilder = Complex.DummyMessage.newBuilder();
        dBuilder.setId(id)
                .setName(name);
        return dBuilder.build();
    }
}
