# hexaAndMapping-lib-Pd

### What is this repository for? ###

* This repository contains abstractions with GUI for pure data software. These abstractions deals with audio effects and mapping elements to control hardware guitar effects. The architecture of this patch is based on Automatonism (https://www.automatonism.com/the-software/). 

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
	* Pd
	* Arduino
* Advice : we'll talk about `default_playground.pd` in the following but we advise to save this under a different name in order to keep a working copy.
* Make abstractions easily dynamically addable to `default_playground.pd`
	* Go to modules selection window
		* Duplicate one of the existing bang
		* Change the label and the send name
	* From main patch go to `abs-creation` subpatch
		* Go inside relevant subpatch (i.e : `hex-effect`) you'll find patches that are used to create dynamically abstractions with GUI. 
		* Duplicate relevant subpatch (i.e : `hex-delay`) and get inside that subpatch
			* Change the following three elements :
				* The first receive at the top of the page (should be the same name you put in the send of the bang you created on step 1).
				* The send object at the bottom of the page should be `pd-nameofyourpatch.pd`
				* In the middle of the patch there's a message (connected to the second outlet of the trigger) with the name of the object you'll create. Change it to the one you've created.
	* If the patch exists in your folder, you should be able to click on the bang on see it appear on your `default_playground.pd` 
* The only conventions we use for the moment are :
	* End your patch name with a ~ it dels mostly with audio otherwise don't put anything.
	* Hexaphonic FX should be named hex-nameofyoureffect~.pd.		
	* Mono FX should be named mono-nameofyoureffect~.pd.
	* Hexaphonic FX should have their mono counterparts.
	
* Build new audio FX :
	* Hexa :
	* Mono :