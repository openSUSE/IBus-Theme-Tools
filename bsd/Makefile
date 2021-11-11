# Created by: Hollow Man <hollowman@hollowman.ml>

PORTNAME=		ibus-theme-tools
PORTVERSION=	4.2.0
DISTVERSIONPREFIX=	v
CATEGORIES=	deskutils python
DIST_SUBDIR=	python

MAINTAINER=	hollowman@hollowman.ml
COMMENT=		IBus Theme Tools

LICENSE=		GPLv3+
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}tinycss2>=0:textproc/py-tinycss2@${PY_FLAVOR} \
				gettext>=0:devel/gettext

USES=			python:3.6+
USE_PYTHON=	distutils autoplist
USE_GITHUB=	yes

GH_ACCOUNT=	openSUSE
GH_TAGNAME=	6b43bd8
GH_PROJECT=	IBus-Theme-Tools

NO_ARCH=		yes

.include <bsd.port.mk>
