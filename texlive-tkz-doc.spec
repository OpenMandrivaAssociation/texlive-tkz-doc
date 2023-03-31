Name:		texlive-tkz-doc
Version:	63902
Release:	2
Summary:	Documentation macros for the TKZ series of packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tkz-doc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-doc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-doc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle offers a documentation class (tkz-doc) and a
package (tkzexample). These files are used in the documentation
of the author's packages tkz-tab and tkz-linknodes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/tkz-doc

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
