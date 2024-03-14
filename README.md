# Anime Airing Notification System

This project is a simple Python program for managing an anime schedule. It allows users to add, edit, and delete anime entries for each day of the week. The program also provides notifications for upcoming anime airing times.

## Files

* `jsonCode.py` - Contains the main functionality for managing the anime schedule.
* `notification.py` - Provides functions for sending notifications for upcoming anime airing times.
* `schedule.json` - JSON file storing the anime schedule data.

## Features

* **Add Anime** - Allows users to add new anime entries to the schedule.
* **Edit Schedule** - Enables users to edit existing anime entries in the schedule.
* **Delete Anime** - Allows users to delete anime entries from the schedule.
* **Clear Schedule** - Allows users to remove all anime entries from the schedule.
* **Notifications** - Sends notifications for upcoming anime airing times.

## Usage

1. Run `jsonCode.py` to manage the anime schedule.
2. The program will prompt you to choose from the following options:
   * Add Anime
   * Edit Schedule
   * Delete Anime
   * Clear Schedule
3. Follow the prompts to perform the desired action.

Make sure that the main schedule program is not running during the time of making changes.

## Dependencies

* `plyer` - Used for sending desktop notifications.
