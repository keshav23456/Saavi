import 'package:flutter/material.dart';
import 'package:flutter_swipe_detector/flutter_swipe_detector.dart';
import 'package:saavi/screens/first_launch/page3.dart';
import 'package:saavi/screens/first_launch/page1.dart';
import 'package:saavi/screens/sign_in.dart';

class Page2 extends StatelessWidget {
  const Page2({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.white,
        actions: [
          GestureDetector(
            onTap: () {
              Navigator.pushReplacement(context,
                  MaterialPageRoute(builder: (context) => const SignIn()));
            },
            child: const Padding(
              padding: EdgeInsets.all(8.0),
              child: Text(
                'Skip >',
                textAlign: TextAlign.right,
                style: TextStyle(
                  color: Colors.black,
                  fontSize: 18,
                  fontFamily: 'Roboto',
                  fontWeight: FontWeight.w900,
                  height: 0,
                ),
              ),
            ),
          )
        ],
      ),
      backgroundColor: Colors.white,
      body: DecoratedBox(
        decoration: const BoxDecoration(
          image: DecorationImage(
              image: AssetImage("assets/images/bg1.png"), fit: BoxFit.cover),
        ),
        child: SwipeDetector(
          onSwipeLeft: (offset) {
            Navigator.pushReplacement(context,
                MaterialPageRoute(builder: (context) => const Page3()));
          },
          onSwipeRight: (offset) {
            Navigator.pushReplacement(context,
                MaterialPageRoute(builder: (context) => const Page1()));
          },
          child: SizedBox.expand(
            child:
                Column(mainAxisAlignment: MainAxisAlignment.center, children: [
              Image.asset("assets/images/firstLaunch2.png"),
              const SizedBox(
                height: 50,
              ),
              const Text(
                'Fast Charging',
                textAlign: TextAlign.center,
                style: TextStyle(
                  color: Color(0xFFCA2572),
                  fontSize: 22,
                  fontFamily: 'Roboto',
                  fontWeight: FontWeight.w600,
                  height: 0,
                ),
              ),
              const SizedBox(
                height: 20,
              ),
              const Text(
                'Access fast charging options to power up your EV in minutes',
                textAlign: TextAlign.center,
                style: TextStyle(
                  color: Color(0xFF80869A),
                  fontSize: 16,
                  fontFamily: 'Roboto',
                  fontWeight: FontWeight.w400,
                ),
              ),
              const SizedBox(
                height: 20,
              ),
              const Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(size: 15, Icons.circle_outlined),
                  Icon(size: 15, Icons.circle),
                  Icon(size: 15, Icons.circle_outlined),
                  Icon(size: 15, Icons.circle_outlined),
                  Icon(size: 15, Icons.circle_outlined),
                  Icon(size: 15, Icons.circle_outlined),
                ],
              ),
            ]),
          ),
        ),
      ),
    );
  }
}
