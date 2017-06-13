# Cleaning and Publishing SHARE Metadata
### Hands on tutorial with OpenRefine
**Thursday, June 15th, Noon - 2 PM Pacific**

[Christina Harlow (Stanford University)](http://www.twitter.com/cm_harlow)

cmharlow@stanford.edu

## Agenda
1. Introduction to OpenRefine
    - About
    - Extensions
    - GLAM Metadata & LOD in OpenRefine
    - Resources
2. Import Data
    - CSV, Google Sheets
    - JSON, XML
    - API or OAI-PMH Data (taken from SHARE Examples)
    - RDF/XML, RDF Ntriples
3. Data Remediation/Munging
    - Splitting & Merging Columns, Rows
    - Faceting, Clustering
    - GREL for Text, Numbers, Dates
    - Regular Expressions
    - Example: Date Formats; Personal Names;
4. Reconciliation
    - Add a column/hit APIs
    - Standard Reconciliation Services
    - Geonames, LCNAF, LCSH Reconciliation
    - Capturing URIs or Identifiers
5. Publishing your Normalized / Enhanced Metadata
    - What data representation and format do you need out?
    - Publishing CSV, JSON, XML for reloading or overlay into your system
    - Sharing full OpenRefine projects containing your data.
6. Questions, Possible Breakouts/New Directions
    - Reconciliation without OpenRefine
    - Building LDF Server for OpenRefine recon
    - Building Recon Services

## Working with Examples
By the end, we won't have *perfect* or *complete* remediated metadata files, but we'll know how to get there and have started on this work. I will have metadata taken from the SHARE API to work with, but also invite participants to bring their own metadata files or datasets to work on.

## Contents of this Repository
- Slides & Speaker's Notes
- OpenRefine Installation Instructions
- Procedures Documentation (for use later in your own documentation)
- Sample Data & Projects Used

## Participant Requirements

We request that all participants have their own laptop or computer to work on, preferably one that you have installation or admin privileges on (if possible). The laptop should have OpenRefine (see below) installed as well as an up-to-date modern web browser (basically, not Internet Explorer).

Please have the latest release candidate (2.7rc2, albeit 2.6 and 2.7rc1 should also work) of OpenRefine installed before the start of the workshop. Instructions for installation are available at [Installation](Installation/README.md). If you run into any issues with installation, please get in touch with [me](mailto:cmharlow@stanford.edu) as soon as you are able, and I'll work through these issues with you. Note the back-up options as well.

## Expectations of Participants

In order to create an inclusive, safe, and open work environment, we ask that all participants follow a [set of rules designed by the the Recurse Center, previously the Hacker School](recurse.com/manual#sub-sec-social-rules). In their own words, *'the goal [of the Recurse Center Social Rules] isn't to burden everyone with a bunch of annoying rules, or to give us a stick to bludgeon people with for "being bad." Rather, these rules are designed to help all of us build a pleasant, productive, and fearless community.'*

As such, these four rules are a lightweight set of explicit social norms to curtail specific kinds of behavior found to be destructive to a supportive, productive, and fun learning/working environment. The four rules are listed here; you can read more about them at http://recurse.com/manual#sub-sec-social-rules.

1. "No feigning surprise." You shouldn't act surprised when someone says they don't know something. There is no benefit to feigning surprise, and regardless of intent, it makes someone feel bad, or worse, about admitting that they don't know something.
2. "No well-actually's." This is when someone says something almost, but not entirely correct, and another person responds with "well, actually," and gives a correction. That's not to say we don't care about truth or precision, but there are better ways to communicate this.
3. "No back-seat driving." If you overhear other people working through a problem, don't just intermittently toss advice in without engaging.
4. "No subtle -isms". This last rule bans racism, sexism, homophobia, transphobia, and other kinds of bias. Subtle -isms are small things that make others feel uncomfortable, and might be familiar as they're under the term "microagressions."
