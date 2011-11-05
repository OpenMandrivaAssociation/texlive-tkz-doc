# revision 22959
# category Package
# catalog-ctan /macros/latex/contrib/tkz-doc
# catalog-date 2011-06-05 23:10:23 +0200
# catalog-license lppl
# catalog-version 1.1c
Name:		texlive-tkz-doc
Version:	1.1c
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3

%description
This bundle offers a documentation class (tkz-doc) and a
package (tkzexample). These files are used in the documentation
of the author's packages tkz-tab and tkz-linknodes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tkz-doc/tkz-doc.cls
%{_texmfdistdir}/tex/latex/tkz-doc/tkzexample.sty
%doc %{_texmfdistdir}/doc/latex/tkz-doc/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
