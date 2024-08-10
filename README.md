# Health App

## Overview

The Health App is a command-line tool designed to help users record, store, and analyze various health-related measurements. It supports multiple types of records including body measurements, exercises, medications, and nutrition. This app is currently under development and is intended to be a flexible and extensible solution for personal health tracking.

## Features

- **User Management**: Create and manage multiple user profiles.
- **Body Measurements**: Record measurements like weight, height, and blood pressure.
- **Exercise Tracking**: Track weightlifting and cardio exercises. Add new exercises dynamically.
- **Medication Tracking**: Record and manage medications with dosage information.
- **Nutrition Logging**: Log nutritional intake categorized by meal types.
- **Configurable Menus**: Menus are dynamically loaded from and saved to JSON files, allowing easy updates and extensions.
- **Flexible Units**: Supports both metric and imperial units.

## Installation

To use the Health App, clone the repository and run the script using Python 3.x. Make sure you have the required dependencies installed.

```bash
git clone https://github.com/yourusername/health-app.git
cd health-app
```

Ensure you have Python 3 installed. You can then run the app with:

```bash
python health.py
```

## Usage

Upon starting the app, you'll be presented with the main menu. From there, you can:

1. Add User: Create a new user profile.
2. Configure Settings: (Feature under development)
3. Exercise Menu: Record and manage exercise records. Add new exercises as needed.
4. Body Measurements Menu: Log body measurements.
5. Medication Menu: Record and manage medications.
6. Nutrition Menu: Log nutritional intake.
7. View Health Records: View recorded health data.
8. Exit: Exit the application.

## Adding New Items
You can dynamically add new exercises, body measurements, and medications through their respective menus. The app will update the menus and records accordingly.

## Development Status
This application is under active development. New features and improvements will be added over time. The current version supports basic functionality and allows for dynamic updates to menus and records.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.


