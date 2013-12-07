# revision 22959
# category Package
# catalog-ctan /macros/latex/contrib/tkz-doc
# catalog-date 2011-06-05 23:10:23 +0200
# catalog-license lppl
# catalog-version 1.1c
Name:		texlive-tkz-doc
Version:	1.1c
Release:	4
Summary:	Documentation macros for the TKZ series of packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tkz-doc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-doc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-doc.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/tkz-doc/tkz-doc.cls
%{_texmfdistdir}/tex/latex/tkz-doc/tkzexample.sty
%doc %{_texmfdistdir}/doc/latex/tkz-doc/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1c-2
+ Revision: 756976
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1c-1
+ Revision: 719762
- texlive-tkz-doc
- texlive-tkz-doc
- texlive-tkz-doc

