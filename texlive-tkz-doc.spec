%global tl_name tkz-doc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.45c
Release:	%{tl_revision}.1
Summary:	Documentation macros for the TKZ series of packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tkz-doc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-doc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-doc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle offers a documentation class (tkz-doc) and a package
(tkzexample). These files are used in the documentation of the author's
packages tkz-base, tkz-euclide, tkz-fct, tkz-linknodes, and tkz-tab.

