# LanguagePackConverter
Converting Traditional Chinese Language Packs to Simplified


- Currently supports converting XML files with traditional chinese inner text to simplified
- Requires:
  - Python3
  - hanzicov

- Script has not been generalized, it is written specificly for converting the language packs formatted for Civilization 5. The following description will help you modify the script to suit your needs. A generalized converter will be added in the future.

- Using the converter:
  - Copy the the language pack folder
    - In the case of CIV 5 this is likely located at located at "C:\Program Files (x86)\Steam\steamapps\common\Sid Meier's Civilization V\Assets\Gameplay\XML\NewText\ZH_Hant_HK"
  - In a new directory, paste the language pack folder and create a new separate directory called "NewPack"
  - Paste another copy of the language pack folder into "NewPack"
  - Run the python script in your current directory (should have subdirectories "NewPack" and "ZH_Hant_HK")
  - "NewPack" should now contain a converted version of ZH_Hant_HK. Copy this file and use it to replace the original "ZH_Hant_HK" file, in its original location.
  - Start the game and in game text (with a few exceptions such as the initial loading screen) should be in Simplified Chinese
  
  
 - In the future I will likely make a script that iterates through all game files and that works for any steam game. This is just what I was able to whip up in an hour or so. Enjoy.
