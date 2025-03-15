import org.gradle.api.JavaVersion

plugins {
    id("com.android.application")
    // START: FlutterFire Configuration
    id("com.google.gms.google-services")
    // END: FlutterFire Configuration
    id("kotlin-android")
    // The Flutter Gradle Plugin must be applied after the Android and Kotlin Gradle plugins.
    id("dev.flutter.flutter-gradle-plugin")
}

android {
    namespace = "com.example.wesalvator"
    compileSdk = flutter.compileSdk!! // Ensure it's properly resolved

    defaultConfig {
        applicationId = "com.example.wesalvator"
        minSdk = 23
        targetSdk = flutter.targetSdk!! // Ensure proper resolution
        versionCode = flutter.versionCode!!
        versionName = flutter.versionName!!
    }

    buildTypes {
        release {
            signingConfig = signingConfigs.debug // ✅ Fix signing config
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
    }

    ndkVersion = "27.0.12077973" // ✅ Move it to the correct position
}

flutter {
    source = "../.."
}
