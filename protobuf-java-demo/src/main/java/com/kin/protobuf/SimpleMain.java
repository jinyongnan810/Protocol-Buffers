package com.kin.protobuf;

import example.simple.Simple;
import example.simple.Simple.SimpleMessage;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Arrays;

public class SimpleMain {
    public static void main(String[] args) throws IOException {
        System.out.println("hello world");
        // create object
        SimpleMessage.Builder builder = SimpleMessage.newBuilder();
        builder.setId(12)
                .setName("test name")
                .setIsSimple(true);
        builder.addSampleList(7)
                .addSampleList(8)
                .addSampleList(9);
        builder.addAllSampleList(Arrays.asList(1, 2, 3));
        // build object
        SimpleMessage msg = builder.build();
        System.out.println(msg.toString());
        // write proto buffer to a binary file
        FileOutputStream os = new FileOutputStream("simple.bin");
        msg.writeTo(os);
        os.close();
        // proto buffer to bytes
        byte[] bytes = msg.toByteArray();


        // read data from binary
        FileInputStream is = new FileInputStream("simple.bin");
        SimpleMessage receivedFromFile = SimpleMessage.parseFrom(is);
        System.out.println(receivedFromFile);
        is.close();
        // read data from bytes
        SimpleMessage receivedFromBytes = SimpleMessage.parseFrom(bytes);
        System.out.println(receivedFromBytes);
    }
}
