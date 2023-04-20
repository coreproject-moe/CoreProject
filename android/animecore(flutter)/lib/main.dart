import 'package:flutter/material.dart';

// https://youtu.be/VPvVD8t02U8?t=32390

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(MaterialApp(
    title: 'Flutter Demo',
    theme: ThemeData(
      primarySwatch: Colors.blue,
    ),
    home: const HomePage(),
  ));
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  late final TextEditingController _email;
  late final TextEditingController _password;

  @override
  void initState() {
    _email = TextEditingController();
    _password = TextEditingController();
    super.initState();
  }

  @override
  void dispose() {
    _email.dispose();
    _password.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      builder: (context, snapshot) {
        return Scaffold(
          appBar: AppBar(
            title: const Text("Register"),
            backgroundColor: Colors.black,
          ),
          body: Column(
            children: [
              TextField(
                enableSuggestions: false,
                autocorrect: false,
                keyboardType: TextInputType.emailAddress,
                decoration: const InputDecoration(hintText: 'Enter your email'),
                controller: _email,
              ),
              TextField(
                obscureText: true,
                enableSuggestions: false,
                autocorrect: false,
                decoration:
                    const InputDecoration(hintText: 'Enter your Password'),
                controller: _password,
              ),
              TextButton(
                onPressed: () async {
                  // final email = _email.text;
                  // final password = _password.text;
                },
                child: const Text("Register"),
              ),
            ],
          ),
        );
      },
    );
  }
}
