package com.kin.protobuf;

import example.enumerations.EnumDemo;
import example.enumerations.EnumDemo.EnumMessage;
import example.enumerations.EnumDemo.DayOfTheWeek;
public class EnumMain {
    public static void main(String[] args) {
        System.out.println("enum demo..");
        EnumMessage.Builder builder = EnumMessage.newBuilder();
        builder.setId(7)
                .setDayOfTheWeek(DayOfTheWeek.FRIDAY);
        EnumMessage msg = builder.build();
        System.out.println(msg);
    }
}
