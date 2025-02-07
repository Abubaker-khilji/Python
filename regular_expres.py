import re

pattern = "was"

text = '''John Silva Meehan (February 6, 1790 – April 24, 1863) was an American publisher, printer, and newspaper editor. Born in New York City, he served in the U.S. Navy during the War of 1812. He then moved to Philadelphia, publishing a Baptist religious journal. When the firm moved to Washington, D.C., in 1822, Meehan edited and published a Baptist weekly newspaper. In late 1825 he purchased the City of Washington Gazette, renaming it the United States' Telegraph and taking a partisan stance. He was appointed as Librarian of Congress in 1828. A large fire in December 1851 destroyed much of the Library of Congress's collection; Meehan oversaw its reconstruction. The election of Abraham Lincoln prompted Meehan's removal in 1861, and he died suddenly in 1863. Historians were critical of Meehan's tenure, noting that he deferred to the Joint
 Committee on the Library for policy, did not change the library's catalog system, and failed to make progress in transforming the institution into a true national'''


matches = re.finditer(pattern,text)
for match in matches :
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])